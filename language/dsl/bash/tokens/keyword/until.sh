until nslookup mydb; do
  echo "Waiting for mydb"
  sleep 2
done

# ---------------

http_request=(
  curl https://httpbin.org/post
  -s
  -X POST
  -H "Content-Type: application/json"
  -d '{
        "key": "value"
      }'
)

until response=$("${http_request[@]}"); do
  echo "Waiting for service to be available..."
  sleep 2
done

echo "Service responded successfully!"
echo "Response:"
echo
echo "$response"
