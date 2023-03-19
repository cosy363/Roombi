package roombi.server.heart.service;

import roombi.server.heart.dto.HeartlistDto;
import roombi.server.heart.jpa.HeartlistEntity;

public interface HeartService {
    HeartlistDto heart(HeartlistDto heartlistDto);

    HeartlistDto unheart(HeartlistDto heartlistDto);

    Iterable<HeartlistEntity> getHeartlistbyUserNumber(String UserId);
}
