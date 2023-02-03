FROM openjdk:17-ea-11-jdk-slim
VOLUME /tmp
COPY target/naming-1.0.jar NamingServer.jar
ENTRYPOINT ["java", "-jar", "NamingServer.jar"]