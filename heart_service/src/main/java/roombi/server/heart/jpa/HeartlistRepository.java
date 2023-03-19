package roombi.server.heart.jpa;

import org.springframework.data.repository.CrudRepository;
import roombi.server.heart.dto.HeartlistDto;

import java.util.List;

public interface HeartlistRepository extends CrudRepository<HeartlistEntity, Long> {
    List<HeartlistEntity> findByUserNumber(String userNumber);
}
