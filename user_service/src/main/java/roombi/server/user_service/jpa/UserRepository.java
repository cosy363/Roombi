package roombi.server.user_service.jpa;

import org.springframework.data.repository.CrudRepository;

public interface UserRepository extends CrudRepository<UserEntity, Long> {
    UserEntity findByUserNumber(String userNumber);
    UserEntity findByUserId(String username);
}
