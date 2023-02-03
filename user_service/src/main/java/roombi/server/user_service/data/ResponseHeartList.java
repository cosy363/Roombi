package roombi.server.user_service.data;

import lombok.Data;

import java.io.Serializable;
import java.util.Date;

@Data
public class ResponseHeartList implements Serializable {
    private String combinationId;
    private String userNumber;

    private Integer totalPrice;
    private Date createdAt;

    private String requestId;

}