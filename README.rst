athena-type-converter
=====================

.. _APL2: http://www.apache.org/licenses/LICENSE-2.0.txt
.. _AWS Athena: https://docs.aws.amazon.com/athena/latest/ug/what-is.html
.. _boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html
.. _get_query_results: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_query_results

A libary of convertors for `AWS Athena`_ results. This greatly simplifies
handling of results returned from `boto3`_ `get_query_results`_ calls.

Installation
------------
``pip install athena-type-converter``

Usage
-----

This will convert all the contained ResultSet into a ``list`` of
``dict``'s, where the dictionary keys are the column names, and the
values are converted to Python value equivalents.

  .. code-block:: python

    from athena_type_converter import convert_result_set
    from boto3 import client

    athena = client('athena')
    query_execution_id = athena.start_query_execution(...)
    response = athena.get_query_results(
      QueryExecutionId=query_execution_id
    )
    results = convert_result_set(response['ResultSet']

More sophisticated usage is exposed, including the complete list of
type converters by `AWS Athena`_ type names.

License: `APL2`_
