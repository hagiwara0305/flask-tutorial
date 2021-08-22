FROM amazonlinux

COPY ./app/* /var/project-flask/

WORKDIR /var/project-flask

RUN amazon-linux-extras install -y python3.8 \
&&  yum install python \
&&  echo 'alias python=python3.8' >> ~/.bashrc \
&&  echo 'alias pip=pip3.8' >> ~/.bashrc \
&&  source ~/.bashrc \
&&  pip3.8 install -r requirements.txt

# EXPOSE 80

CMD python3.8 app.py &