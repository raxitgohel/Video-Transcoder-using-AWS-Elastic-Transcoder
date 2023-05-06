# Video-Transcoder-using-AWS-Elastic-Transcoder
This is a Video Transcoder implementation made with Python-Flask. I used AWS Elastic Transcoder for transcoding videos and S3 Buckets to Store it.

### Create S3 Buckets
I have created two AWS S3 buckets, one for input and other for output. You can use only one to store both input and transcoded videos also.
Note the names of bucket, I have mentioned them as <INPUT_VIDEO_BUCKET> and <OUTPUT_VIDEO_BUCKET>.

### Create AWS Elastic Transcoder pipeline.
To create a new pipeline, you'll need to give input and output bucket names and storage class there,
I chose Standard class. Leave IAM Role at default. Ignore optional fields. Click Create Pipeline. Note the Pipleline ID, which will be
in place of <PIPELINE_ID> in app.py. You may check whether the pipeline is working properly by uploading a video file in input bucket and then creating a job from elastic transcoder dashboard.

### Implement jobs in Flask web-app using Python
To do this, you need to use AWS SDK for python(boto3).
You can find more info about using boto3 from [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html).

Create a virtual environment.
`python -m venv envname`

Install all the requirements.
`pip install -r requirements.txt`

You also need to set AWS ACCESS KEY ID and AWS SECRET ACCESS KEY. It can be done in a number of ways.

Write it directly into code(**Make Sure to deactivate keys after use**)

`os.environ['AWS_ACCESS_KEY_ID'] = 'access_key_id'`

`os.environ['AWS_SECRET_ACCESS_KEY'] = 'access_secret_key'`

You can set it through terminal also.

After this you can run app.py using this command.
`python app.py`
