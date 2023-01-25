package roombi.server.user_service.controller;

import org.modelmapper.ModelMapper;
import org.modelmapper.convention.MatchingStrategies;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import roombi.server.user_service.data.RequestUser;
import roombi.server.user_service.data.ResponseUser;
import roombi.server.user_service.data.Welcome;
import roombi.server.user_service.dto.UserDto;
import roombi.server.user_service.jpa.UserEntity;
import roombi.server.user_service.service.UserService;

import javax.servlet.http.HttpServletRequest;

@RestController
@RequestMapping("/")
public class UserController {
    private Environment environment;
    private UserService userService;

    @Autowired
    private Welcome welcome;

    @Autowired
    public UserController(Environment environment, UserService userService) {
        this.environment = environment;
        this.userService = userService;
    }

    @GetMapping("/healthcheck")
    public String status(HttpServletRequest httpServletRequest) {
        return String.format("User Service Working" +
                ", Local Server Port = " + environment.getProperty("local.server.port")
                + ", Server Port = " + environment.getProperty("server.port")
                + ", Token = " + environment.getProperty("token.secret")
                + ", Token Exp. at = " + environment.getProperty("token.expiration_time"));
    }


    @GetMapping("/welcome")
    public String welcome() {
        return "Welcome to User Service MSA";
    }

    @GetMapping("/welcome2")
    public String welcome2() {
        return welcome.getMessage();
    }

    @PostMapping("/users")
    public ResponseEntity createUser(@RequestBody RequestUser user) {
        ModelMapper mapper = new ModelMapper();
        mapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
        UserDto userDto = mapper.map(user, UserDto.class);

        userService.createUser(userDto);

        ResponseUser responseUser = mapper.map(userDto, ResponseUser.class);

        return ResponseEntity.status(HttpStatus.CREATED).body(responseUser);
    }

    @GetMapping("/users/{userNumber}")
    public ResponseEntity<ResponseUser> getUser(@PathVariable("userNumber") String userNumber) {
        UserDto userDto = userService.getUserByUserNumber(userNumber);

        ResponseUser returnValue = new ModelMapper().map(userDto, ResponseUser.class);

        return ResponseEntity.status(HttpStatus.OK).body(returnValue);
    }
}
