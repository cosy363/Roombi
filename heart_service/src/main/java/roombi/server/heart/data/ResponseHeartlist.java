package roombi.server.heart.data;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;

import java.util.List;

@Data
@JsonInclude(JsonInclude.Include.NON_NULL)
public class ResponseHeartlist {

    private String userNumber;
    private Long heartId;
    private String combId;
}
