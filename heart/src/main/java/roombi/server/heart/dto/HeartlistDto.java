package roombi.server.heart.dto;

import lombok.Data;

import java.io.Serializable;

@Data
public class HeartlistDto implements Serializable {
    private String userNumber;
    private Long heartId;
    private String combId;

}
