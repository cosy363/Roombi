package roombi.server.user_service.service;

import org.apache.catalina.Store;
import org.modelmapper.ModelMapper;
import org.modelmapper.convention.MatchingStrategies;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import roombi.server.user_service.data.ResponseHeartList;
import roombi.server.user_service.dto.UserDto;
import roombi.server.user_service.jpa.UserEntity;
import roombi.server.user_service.jpa.UserRepository;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Service
public class UserServiceImpl implements UserService {
    UserRepository userRepository;
    BCryptPasswordEncoder passwordEncoder;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        UserEntity userEntity = userRepository.findByUserId(username);

        if (userEntity == null) {
            throw new UsernameNotFoundException(username);
        }
        return new User(userEntity.getUserId(), userEntity.getEncryptedPwd(),
                true, true, true, true, new ArrayList<>());
    }

    @Autowired
    public UserServiceImpl(UserRepository userRepository, BCryptPasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public UserDto createUser(UserDto userDto) {
        userDto.setUserNumber(UUID.randomUUID().toString());

        //Mapping with JPA
        ModelMapper modelMapper = new ModelMapper();
        modelMapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
        UserEntity userEntity = modelMapper.map(userDto, UserEntity.class);

        userEntity.setEncryptedPwd(passwordEncoder.encode(userDto.getPwd()));

        userRepository.save(userEntity);

        return null;
    }

    @Override
    public UserDto getUserByUserNumber(String userNumber) {
        UserEntity userEntity = userRepository.findByUserNumber(userNumber);
        System.out.println("UserServiceImpl.getUserByUserNumber");
        if (userEntity == null) {
            throw new UsernameNotFoundException("User not found");
        }

        UserDto userDto = new ModelMapper().map(userEntity, UserDto.class);

        //Get HeartList
        List<ResponseHeartList> heartLists = new ArrayList<>();
        String heartlistUrl = "http://127.0.0.1:8000/heart-service/%s/heartlist";


        userDto.setHeartLists(heartLists);

        return userDto;
    }

    @Override
    public UserDto getUserDetailsByUserNumber(String userId) {
        UserEntity userEntity = userRepository.findByUserId(userId);

        if (userEntity == null) {
            throw new UsernameNotFoundException(userId);
        }

        UserDto userDto = new ModelMapper().map(userEntity, UserDto.class);
        return userDto;

    }
}
