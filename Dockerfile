# use base python image with python 2.7
FROM python:3.7


#RUN pipreqs --force ./

WORKDIR /celery_task/
# add requirements.txt to the image
ADD requirements.txt /celery_task/requirements.txt

# set working directory to /app/

# install python dependencies
RUN pip3 install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com -r requirements.txt

COPY . /celery_task

ADD run.sh  /run.sh

RUN chmod +x /run.sh

EXPOSE 5000

ENTRYPOINT ["/run.sh"]