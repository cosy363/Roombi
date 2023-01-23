package roombi.server.user_service.jpa;

import lombok.Data;
import javax.persistence.*;

@Data
@Entity
@Table(name="users")
public class UserEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 50)
    private String userId;

    @Column(nullable = false, length = 50, unique = true)
    private String userNumber;

    @Column(nullable = false, length = 50, unique = true)
    private String encryptedPwd;
}
