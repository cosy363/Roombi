package roombi.server.naming;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@SpringBootApplication
@EnableEurekaServer
public class NamingApplication {

	public static void main(String[] args) {
		SpringApplication.run(NamingApplication.class, args);
	}

}
