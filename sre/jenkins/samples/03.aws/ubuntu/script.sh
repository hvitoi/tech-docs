#/bin/bash

MYSQL_HOST=$1
MYSQL_PASSWORD=$2
MYSQL_DATABASE=$3
AWS_ACCESS_KEY_ID=$4
AWS_SECRET_ACCESS_KEY=$5
AWS_BUCKET_NAME=$6
BACKUP_NAME=db-$(date +%H-%M-%S).sql

# Create a backup for the database
mysqldump -u root -h $MYSQL_HOST -p$MYSQL_PASSWORD $MYSQL_DATABASE > /tmp/$BACKUP_NAME && \
export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID && \
export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY && \
echo "Uploading your db backup..." && \
aws s3 cp /tmp/$BACKUP_NAME s3://$AWS_BUCKET_NAME/$BACKUP_NAME

# Copy the script into the Pod
# docker container cp script.sh remote-host:/tmp/script.sh

# Run script
# /tmp/script.sh $MYSQL_HOST $MYSQL_PASSWORD $MYSQL_DATABASE $AWS_ACCESS_KEY_ID $AWS_SECRET_ACCESS_KEY $AWS_BUCKET_NAME
# /tmp/script.sh db-host 123 testdb asdf asdf hvitoi
