package roombi.server.user_service.service;

import org.springframework.security.core.userdetails.UserDetailsService;
import roombi.server.user_service.dto.UserDto;

public interface UserService extends UserDetailsService {
    UserDto createUser(UserDto userDto);
    UserDto getUserByUserNumber(String userNumber);
    UserDto getUserDetailsByUserNumber(String userId);

}
