# Roombi
Spring+FASTAPI based Furniture Combination Generator

  <br>
  <img src="./images/Roombi.png" style="width:300px;height:300px;>
  <br>

  <p>
- 사용자의 취향에 따라 4가지 종류의 가구를 추천해주는 RestAPI 기반의 Application입니다.
  -> 추천 알고리즘은 기존에 설정된 추천 점수표에 따라 작동하는 조합 알고리즘, 그리고 조합 알고리즘에 의해 만들어진
     조합을 평가하는 딥러닝 알고리즘이 있습니다.
  -> 선호 가구 종류, 선호 색상, 예산을 Input으로 받으며, 가장 높은 점수를 받은 20개의 가구 조합을 생성합니다.
  -> 가구 데이터베이스는 IKEA의 카탈로그를 참조했습니다.
  
- MSA화 
- 사용자의 취향 및 예산 Input에 따라 4가지 종류의 가구를 추천해주는 Application입니다. 하
- 사용자의 취향 및 예산 Input에 따라 4가지 종류의 가구를 추천해주는 Application입니다.  

  </p>

## 프로젝트 소개

<p align="justify">
프로젝트 개요/동기
</p>

<p align="center">
GIF Images
</p>

<br>

## 기술 스택

###Spring MSA(User Microservice & Heart Microservice)
Java 11
Spring Boot 2.7.8
Spring Cloud 3.1.4
JJWT 0.9.1
Eureka Server, Client
  
###Combination Microservice 
Python 3.10.9
Flask 2.2.2
PyJWT 2.6
py-eureka-client 0.16.0

###Etc.
Git
RabbitMQ
Prometheus
Zipkin
Grafana


<br>

## 구현 기능

### User Service

### Heart Service

### Combination Service
- Flask 
  
### WebScrapper


<br>

## To be updated in version 2

<p align="justify">

</p>

<br>
