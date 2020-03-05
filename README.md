# app-function-uploader

#### A command line tool for uploading AppSync functions into AWS AppSync

This is intended to be used in a CI/CD process for managing AppSync functions.

The function's name and datasource are used to look up the unique function id. Failure to have this combination return one function will result in undefined behavior.

### Usage
```
python -m appsync_function_uploader --aws-access-key-id accesskey --aws-secret-access-key secret --aws-region region --api-id id --name name --description description --datasource-name datasource --request-mapping-template request.vtl --response-mapping-template response.vtl 
```

### Arguments
- **aws-access-key-id** The AWS Access Key ID for the IAM user
- **aws-secret-access-key** The AWS Secret Access Key for the IAM user
- **aws-region** The AWS Region of the AppSync API to update
- **api-id** The API ID of the AppSync API to upload the schema to
- **name** The Function name - does not have to be unique, but it is highly recommended
- **description** The Function description
- **datasource-name** The name of the AppSync data source for which the function is being created
- **request-mapping-template** The request mapping VTL file to upload
- **response-mapping-template** The response mapping VTL file to upload
