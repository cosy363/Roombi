package roombi.server.combination.jpa;

import org.springframework.data.repository.CrudRepository;

public interface CombRepository extends CrudRepository<CombEntity, Long> {
    Iterable<CombEntity> findByUserId(String userId);


}
