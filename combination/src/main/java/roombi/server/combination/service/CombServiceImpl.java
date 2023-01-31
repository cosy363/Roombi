package roombi.server.combination.service;

import org.modelmapper.ModelMapper;
import org.modelmapper.convention.MatchingStrategies;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import roombi.server.combination.dto.CombDto;
import roombi.server.combination.jpa.CombEntity;
import roombi.server.combination.jpa.CombRepository;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Service
public class CombServiceImpl implements CombService {
    CombRepository combRepository;
    RestTemplate restTemplate;
    Environment env;

    @Autowired
    public CombServiceImpl(CombRepository combRepository,
                           RestTemplate restTemplate,
                           Environment env) {
        this.combRepository = combRepository;
        this.restTemplate = restTemplate;
        this.env = env;
    }

    @Override
    public CombDto GenerateCombination(CombDto combDto) {

        /// API CALL to Flask Server
        String combinationUrl = "http://127.0.0.1:5001/flask-service/combination/getcombination";
        restTemplate.postForObject(combinationUrl, HttpMethod.POST, )

//        RestTemplate restTemplate = new RestTemplate();
//        ResponseEntity<String> responseEntity = restTemplate.exchange("http://localhost:5000/abstractive", HttpMethod.POST,
//                entity, String.class);


        /// Get Details from each Product ID
        ModelMapper modelMapper = new ModelMapper();
        modelMapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);

        CombEntity combEntity = modelMapper.map(combDto, CombEntity.class);

        //Return Combination Result to Controller
        CombDto combDtoReturn = new ModelMapper().map(combEntity, CombDto.class);

        return combDtoReturn;
    }

}

