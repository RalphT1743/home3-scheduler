import json
import logging
from datetime import datetime, timezone

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
  """ Reminder for Appointments  """
  request_id = getattr(context, "aws_request_id", "unknown")

logger.info(json.dumps({
  "service": "home3-scheduler",
  "event": "lambda_invoked",
  "requestId": request_id, 
  "timestamp": datetime.now(timezone.utc).isoformat(),
  "payload": event
}))

logger.info(json.dumps({
  "service":"home3-scheduler",
  "event":"lambda_completed",
  "requestId": request_id,
  "status":"success"
}))

return{
  "statusCode":200,
  "body": "Reminder processed"
}
                      
