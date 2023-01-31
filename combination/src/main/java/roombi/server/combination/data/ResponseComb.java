package roombi.server.combination.data;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;

@Data
@JsonInclude(JsonInclude.Include.NON_NULL)
public class ResponseComb {
    private Integer productId1;
    private Integer productId2;
    private Integer productId3;
    private Integer productId4;
    private String userId;

    private String ImageUrlProductId1;
    private String ImageUrlProductId2;
    private String ImageUrlProductId3;
    private String ImageUrlProductId4;

    private Integer totalPrice;

}
