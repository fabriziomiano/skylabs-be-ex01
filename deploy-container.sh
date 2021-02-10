if heroku apps:create skylabs-ex01 --region eu; then
  echo "App creation succeded"
fi
echo "App creation failed. Trying to deploy anyway"
heroku container:login &&
  docker build --rm -t api.skylabs:latest . &&
  docker tag api.skylabs:latest registry.heroku.com/skylabs-ex01/web &&
  docker push registry.heroku.com/skylabs-ex01/web &&
  heroku container:push web -a skylabs-ex01 &&
  heroku container:release web -a skylabs-ex01
