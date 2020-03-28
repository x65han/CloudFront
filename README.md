# CloudFront (Your Own CDN)

- Host your static assets on Github and deploy to cloud
- Use file checksum to detect changes
```diff
[Compiling] Version 1
[Found] 2 entries
-[DEL] icon-waterloo.png -> 840718cf5d750b818154b5568586eae1
[Old] icon-facebook.png -> 708018bebb8b7ed725e967023b1468b8
+[New] temp.txt -> d41d8cd98f00b204e9800998ecf8427e
[Saving JSON] /Users/johnson/cloudfront/v1.json
```
- All files has `cache control` set to a `max age of 1 year`, so that browser can take advantage of caching and improve website performance
- Simply place your files in v1/, then run `./deploy.sh`

# Deployment

- Modify & run [deploy.sh](https://github.com/x65han/CloudFront/blob/master/deploy.sh)
```sh
heroku git:remote -a your_app_name
```

- Then access your files @ https://your_app_name.herokuapp.com/static/v1/{md5_hash}.
- [Here's an example](http://stillcloud.herokuapp.com/still/v1/ad2e64cb120f5e0e996ed7cd54749edf). You can view all your files' md5 hash in [v1.json](https://github.com/x65han/CloudFront/blob/master/v1.json)

- Note that Heroku has a 500 mb limit with the free tier. You can opt to deploy to AWS, Azure or Google Cloud for bigger storage size.
