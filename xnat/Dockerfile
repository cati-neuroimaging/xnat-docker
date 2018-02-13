FROM tomcat:7

RUN mkdir -p /data/xnat/home/config &&\
    mkdir /data/xnat/home/logs &&\
    mkdir /data/xnat/home/plugins &&\
    mkdir /data/xnat/home/work &&\
    mkdir /data/xnat/archive &&\
    mkdir /data/xnat/build &&\
    mkdir /data/xnat/cache &&\
    mkdir /data/xnat/ftp &&\
    mkdir /data/xnat/pipeline &&\
    mkdir /data/xnat/prearchive

RUN curl -L -o /usr/local/tomcat/webapps/xnat-web-1.7.4.1.war https://api.bitbucket.org/2.0/repositories/xnatdev/xnat-web/downloads/xnat-web-1.7.4.1.war
RUN mv /usr/local/tomcat/webapps/xnat-web-1.7.4.1.war /usr/local/tomcat/webapps/xnat.war

COPY gradle.properties /tmp/gradle.properties
COPY xnat-conf.properties /data/xnat/home/config/xnat-conf.properties


ENV CATALINA_OPTS="-Dxnat.home=/data/xnat/home"

#RUN curl -L -o /tmp/xnat-pipeline-1.7.4.zip https://api.github.com/repos/NrgXnat/xnat-pipeline-engine/zipball/1.7.4
#RUN cd /tmp && unzip xnat-pipeline-1.7.4.zip
#RUN cd /tmp/xnat-pipeline && ./gradlew
