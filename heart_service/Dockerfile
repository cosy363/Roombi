FROM openjdk:17-ea-11-jdk-slim
VOLUME /tmp
COPY build/libs/heart-1.0.jar HeartService.jar
ENTRYPOINT ["java","-jar","HeartService.jar"]