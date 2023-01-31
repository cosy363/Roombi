package roombi.server.combination.jpa;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;

@Data
@Entity
@Table(name="combination_log")
public class CombEntity implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long combinationNo;

    @Column(nullable = false)
    private Integer productId1;

    @Column(nullable = false)
    private String productId2;

    @Column(nullable = false)
    private String productId3;

    @Column(nullable = false)
    private String productId4;

    @Column(nullable = false)
    private Double singleScoreSum;

    @Column(nullable = false)
    private Double combinationScore;

    @Column(nullable = false)
    private String userId;
}
