package roombi.server.combination.controller;

import org.modelmapper.ModelMapper;
import org.modelmapper.convention.MatchingStrategies;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import roombi.server.combination.data.RequestComb;
import roombi.server.combination.data.ResponseComb;
import roombi.server.combination.dto.CombDto;
import roombi.server.combination.service.CombService;

import javax.servlet.http.HttpServletRequest;

@RestController
@RequestMapping("/comb-service/")
public class CombController {
    private Environment environment;
    private CombService combService;

    @Autowired
    public CombController(Environment environment, CombService combService) {
        this.environment = environment;
        this.combService = combService;
    }

    // Health Check
    @GetMapping("/healthcheck")
    public String status(HttpServletRequest httpServletRequest) {
        return String.format("Combination Service on Port Number: %s", httpServletRequest.getServerPort());
    }

    @GetMapping("/welcome")
    public String welcome() {
        return "Welcome to Combination Service";
    }


    @PostMapping("/generate")
    public ResponseEntity createUser(@RequestBody RequestComb requestComb) {
        ModelMapper mapper = new ModelMapper();
        mapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
        CombDto combDto = mapper.map(requestComb, CombDto.class);

        combService.GenerateCombi(CombDto);

        ResponseComb responseComb = mapper.map(combDto, ResponseComb.class);

        return ResponseEntity.status(HttpStatus.CREATED).body(responseComb
        );
    }

}
