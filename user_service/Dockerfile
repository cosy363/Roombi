FROM 11.0.11_9-jre-openj9-0.26.0-focal
VOLUME /tmp
COPY build/libs/user_service-0.0.1-SNAPSHOT.jar UserService.jar
ENTRYPOINT ["java","-jar","UserService.jar"]