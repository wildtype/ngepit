gcloud beta functions deploy gdrive-watch --runtime python37 --entry-point main --trigger-http --set-env-vars=AUTH_TOKEN=$1,DASHBOARD_HOST=$2
