package roombi.server.combination.jpa;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name="combination_log")
public class CombEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long combination_num;

    @Column(nullable = false, length = 50)
    private String userId;

    @Column(nullable = false, length = 50, unique = true)
    private String userNumber;

    @Column(nullable = false, length = 50, unique = true)
    private String encryptedPwd;
}
