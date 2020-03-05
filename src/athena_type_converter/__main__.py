from __future__ import print_function

import argparse
import atexit
import boto3
import json
import logging
import sys

if sys.argv[0].endswith("__main__.py"):
    sys.argv[0] = "python -m appsync_function_uploader"


@atexit.register
def app_exit():
    logging.getLogger().info("Terminating")


def _parse_command_line_arguments():
    argv_parser = argparse.ArgumentParser()
    argv_parser.add_argument(
        '--aws-access-key-id',
        help='The AWS IAM Access Key ID to use'
    )
    argv_parser.add_argument(
        '--aws-secret-access-key',
        help='The AWS IAM Secret Access Key to use'
    )
    argv_parser.add_argument(
        '--aws-region',
        help='The AWS Region of the AppSync API to update'
    )
    argv_parser.add_argument(
        '--api-id',
        help='The API Id of the AppSync API to update'
    )
    argv_parser.add_argument(
        '--name',
        help='The Function name. The function name does not have to be unique, but it is highly recommended.'
    )
    argv_parser.add_argument(
        '--description',
        help='The Function description.'
    )
    argv_parser.add_argument(
        '--datasource-name',
        help='The name of the AppSync data source for which the function is being created'
    )
    argv_parser.add_argument(
        '--request-mapping-template',
        help='The request mapping VTL file to upload'
    )
    argv_parser.add_argument(
        '--response-mapping-template',
        help='The response mapping VTL file to upload'
    )
    return argv_parser.parse_args()


def main():
    try:
        args = _parse_command_line_arguments()

        # set AWS logging level
        logging.getLogger('botocore').setLevel(logging.ERROR)
        logging.getLogger('boto3').setLevel(logging.ERROR)

        with open(args.request_mapping_template) as vtl:
            request_mapping_template = vtl.read()
        with open(args.response_mapping_template) as vtl:
            response_mapping_template = vtl.read()

        appsync = boto3.client(
            'appsync',
            aws_access_key_id=args.aws_access_key_id,
            aws_secret_access_key=args.aws_secret_access_key,
            region_name=args.aws_region
        )

        print('Searching for existing function')
        function_id = _find_function(appsync, args.api_id, args.name, args.datasource_name)
        if function_id:
            print('Found function, updating')
            response = appsync.update_function(
                apiId=args.api_id,
                name=args.name,
                description=args.description,
                functionId=function_id,
                dataSourceName=args.datasource_name,
                requestMappingTemplate=request_mapping_template,
                responseMappingTemplate=response_mapping_template,
                functionVersion='2018-05-29'
            )
        else:
            print('Function does not exist, creating')
            response = appsync.create_function(
                apiId=args.api_id,
                name=args.name,
                description=args.description,
                dataSourceName=args.datasource_name,
                requestMappingTemplate=request_mapping_template,
                responseMappingTemplate=response_mapping_template,
                functionVersion='2018-05-29'
            )
        print('Function upload complete\n', json.dumps(response, indent=4, sort_keys=True))
    except KeyboardInterrupt:
        print('Service interrupted', file=sys.stderr)
    except Exception as e:
        print('Upload FAILED:', e.message, file=sys.stderr)
        print('')
        raise e


def _find_function(appsync, api_id, name, data_source_name, next_token=None):
    if next_token:
        response = appsync.list_functions(
            apiId=api_id,
            nextToken=next_token
        )
    else:
        response = appsync.list_functions(
            apiId=api_id
        )
    function_id = None
    if 'nextToken' in response:
        function_id = _find_function(appsync, api_id, name, data_source_name, response['nextToken'])
    for function in response['functions']:
        if function['name'] == name and function['dataSourceName'] == data_source_name:
            if function_id:
                raise ValueError('Function name {}, dataSourceName {} tuple is not unique, unable to determine function'.format(name, data_source_name))
            function_id = function['functionId']
    return function_id
        

if __name__ == '__main__':
    main()
