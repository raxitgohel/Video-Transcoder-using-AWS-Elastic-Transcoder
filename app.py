import boto3
from flask import Flask, render_template, request, send_file, redirect, url_for, Response
import os


app = Flask(__name__)
s3 = boto3.client('s3')
et = boto3.client('elastictranscoder', region_name='us-east-1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    outfile = filename.split('.')[0]+'_out.mp4'
    s3.upload_fileobj(file, 'inputvideobucket', filename)
    pipeline_id = '1683130471490-7vb2xr'
    preset_id = request.form['preset']
    job = et.create_job(PipelineId=pipeline_id, Input={'Key': filename}, Output={'Key': outfile, 'PresetId': preset_id})
    job_id = job['Job']['Id']
    status = job['Job']['Status']
    return render_template('status.html', job_id=job_id, status=status)

@app.route('/status/<job_id>')
def status(job_id):
    job = et.read_job(Id=job_id)
    status = job['Job']['Status']
    key = job['Job']['Output']['Key']
    if status == 'Complete':
        return render_template('download.html', key=key)
    else:
        return render_template('status.html', job_id=job_id, status=status)

@app.route('/download/<path:key>')
def download(key):
    try:
        file_obj = s3.get_object(Bucket='outputvideobucket', Key=key)
        file_content = file_obj['Body'].read()
        response = Response(file_content)
        response.headers['Content-Disposition'] = 'attachment; filename=' + key
        return response
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
