BROKER_TRANSPORT = 'sqs'
BOTO_PROVIDER = 'boto-provider'
BROKER_URL = 'sqs://'
CELERY_IGNORE_RESULT = True
BROKER_TRANSPORT_OPTIONS = {
                            'queue_name_prefix': 'nimbostratus-',
                            'region': 'us-west-2',
}