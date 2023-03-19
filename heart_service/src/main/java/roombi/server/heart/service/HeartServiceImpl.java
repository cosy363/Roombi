package roombi.server.heart.service;

import org.modelmapper.ModelMapper;
import org.modelmapper.convention.MatchingStrategies;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import roombi.server.heart.dto.HeartlistDto;
import roombi.server.heart.jpa.HeartlistEntity;
import roombi.server.heart.jpa.HeartlistRepository;

@Service
public class HeartServiceImpl implements HeartService {
    HeartlistRepository heartlistRepository;
    BCryptPasswordEncoder passwordEncoder;


    @Autowired
    public HeartServiceImpl(HeartlistRepository heartlistRepository, BCryptPasswordEncoder passwordEncoder) {
        this.heartlistRepository = heartlistRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public HeartlistDto heart(HeartlistDto heartlistDto) {

        //Mapping with JPA
        ModelMapper modelMapper = new ModelMapper();
        modelMapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
        HeartlistEntity heartlistEntity = modelMapper.map(heartlistDto, HeartlistEntity.class);

        heartlistRepository.save(heartlistEntity);

        return null;
    }

    @Override
    public HeartlistDto unheart(HeartlistDto heartlistDto) {

        //Mapping with JPA
        ModelMapper modelMapper = new ModelMapper();
        modelMapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
        HeartlistEntity heartlistEntity = modelMapper.map(heartlistDto, HeartlistEntity.class);

        Long heartId = heartlistEntity.getHeartId();
        heartlistRepository.deleteById(heartId);

        return null;
    }

    @Override
    public Iterable<HeartlistEntity> getHeartlistbyUserNumber(String userNumber) {
        return heartlistRepository.findByUserNumber(userNumber);
    }
}
