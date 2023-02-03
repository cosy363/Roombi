package roombi.server.heart.jpa;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;

@Data
@Entity
@Table(name="heart_list")
public class HeartlistEntity implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long heartId;

    @Column(nullable = false, length = 50)
    private String userNumber;

    @Column(nullable = false, length = 50, unique = true)
    private String combId;

}