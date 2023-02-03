package roombi.server.heart.controller;

import io.micrometer.core.annotation.Timed;
import org.modelmapper.ModelMapper;
import org.modelmapper.convention.MatchingStrategies;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import roombi.server.heart.data.RequestHeart;
import roombi.server.heart.data.RequestHeartlist;
import roombi.server.heart.data.RequestUnheart;
import roombi.server.heart.data.ResponseHeartlist;
import roombi.server.heart.dto.HeartlistDto;
import roombi.server.heart.jpa.HeartlistEntity;
import roombi.server.heart.service.HeartService;


import javax.servlet.http.HttpServletRequest;
import javax.ws.rs.core.Response;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/")
public class HeartController {
    private Environment environment;
    private HeartService heartService;

    @Autowired
    public HeartController(Environment environment, HeartService heartService) {
        this.environment = environment;
        this.heartService = heartService;
    }

    @GetMapping("/healthcheck")
    @Timed(value = "users.status", longTask = true)
    public String status(HttpServletRequest httpServletRequest) {
        return String.format("User Service Working" +
                ", Local Server Port = " + environment.getProperty("local.server.port")
                + ", Server Port = " + environment.getProperty("server.port")
                + ", Token = " + environment.getProperty("token.secret")
                + ", Token Exp. at = " + environment.getProperty("token.expiration_time"));
    }


    @GetMapping("/welcome")
    @Timed(value = "users.welcome", longTask = true)

    public String welcome() {
        return "Welcome to Heart Service MSA";
    }

    @PostMapping("/heart")
    public ResponseEntity heart(@RequestBody RequestHeart combination) {
        ModelMapper mapper = new ModelMapper();
        mapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
        HeartlistDto heartlistDto = mapper.map(combination, HeartlistDto.class);

        heartService.heart(heartlistDto);

        return ResponseEntity.status(HttpStatus.CREATED).body("Hearted");
    }

    @PostMapping("/unheart")
    public ResponseEntity unheart(@RequestBody RequestUnheart combination) {
        ModelMapper mapper = new ModelMapper();
        mapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
        HeartlistDto heartlistDto = mapper.map(combination, HeartlistDto.class);

        heartService.unheart(heartlistDto);

        return ResponseEntity.status(HttpStatus.OK).body("Unhearted");
    }

    @PostMapping("/heartlist")
    public ResponseEntity<List<ResponseHeartlist>> heartlist(@RequestBody RequestHeartlist requestHeartlist) {
        ModelMapper mapper = new ModelMapper();
        mapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
        HeartlistDto heartlistDto = mapper.map(requestHeartlist, HeartlistDto.class);

        String userNumber = heartlistDto.getUserNumber();

        Iterable<HeartlistEntity> heartlistEntities = heartService.getHeartlistbyUserNumber(userNumber);

        List<ResponseHeartlist> result = new ArrayList<>();
        heartlistEntities.forEach(v->{
            result.add(new ModelMapper().map(v,ResponseHeartlist.class));
        });

        return ResponseEntity.status(HttpStatus.OK).body(result);
    }
}
