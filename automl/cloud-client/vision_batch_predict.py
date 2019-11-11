#!/usr/bin/env python

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def batch_predict(project_id, model_id, input_uri, output_uri):
    """Batch predict."""
    # [START automl_vision_batch_predict]
    from google.cloud import automl

    # TODO(developer): Uncomment and set the following variables
    # project_id = 'YOUR_PROJECT_ID'
    # model_id = 'YOUR_MODEL_ID'
    # input_uri = 'gs://YOUR_BUCKET_ID/path_to_your_input_file.csv'
    # output_uri = 'gs://YOUR_BUCKET_ID/path_to_save_results/'

    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = prediction_client.model_path(
        project_id, 'us-central1', model_id)

    gcs_source = automl.types.GcsSource(
        input_uris=[input_uri])

    input_config = automl.types.BatchPredictInputConfig(gcs_source=gcs_source)
    gcs_destination = automl.types.GcsDestination(
        output_uri_prefix=output_uri)
    output_config = automl.types.BatchPredictOutputConfig(
        gcs_destination=gcs_destination)
    # [0.0-1.0] Only produce results higher than this value
    params = {'score_threshold': '0.8'}

    response = prediction_client.batch_predict(
        model_full_id, input_config, output_config, params)

    print('Waiting for operation to complete...')
    print(u'Batch Prediction results saved to Cloud Storage bucket. {}'.format(
        response.result()))
    # [END automl_vision_batch_predict]
