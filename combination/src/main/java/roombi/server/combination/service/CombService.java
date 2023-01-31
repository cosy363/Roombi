package roombi.server.combination.service;

import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.client.RestTemplate;
import roombi.server.combination.dto.CombDto;

public interface CombService {

    CombDto GenerateCombination(CombDto combDto);

    @Bean
    public RestTemplate getRestTemplate() {
        return new RestTemplate();
    }

}
