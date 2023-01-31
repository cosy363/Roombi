package roombi.server.combination.dto;

import lombok.Data;

import java.util.Date;
import java.util.List;

@Data
public class CombDto {
    public String userId;
    private List<Integer> furniturePreference;
    private List<Integer> colorPreference;
    private Integer budget;

    public String combinationId;
    private String productId1;
    private String productId2;
    private String productId3;
    private String productId4;
    private String ImageUrlProductId1;
    private String ImageUrlProductId2;
    private String ImageUrlProductId3;
    private String ImageUrlProductId4;
    private Integer totalPrice;

    private Date createdAt;

}
