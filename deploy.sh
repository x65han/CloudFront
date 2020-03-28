heroku git:remote -a your_app_name

git add v1
python script/compile.py
git add v1.json
date=`date`
git commit -m "[Deploy] $(date)"
git push
git push heroku master
