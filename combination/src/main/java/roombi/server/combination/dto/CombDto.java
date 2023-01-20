package roombi.server.combination.dto;

import lombok.Data;

import java.util.Date;
import java.util.List;

@Data
public class CombDto {
    public String userNumber;
    public String userId;

    private Date createdAt;

    private String combNumber;
    private List<Integer> furniturePreference;
    private List<Integer> colorPreference;
    private Integer budget;

}
