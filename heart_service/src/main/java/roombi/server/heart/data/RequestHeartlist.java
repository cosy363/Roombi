package roombi.server.heart.data;

import lombok.Data;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

@Data
public class RequestHeartlist {

    @NotNull(message = "ID must not be empty.")
    @Size(min = 2, max = 50, message = "ID must be between 2 and 50 characters.")
    private String userNumber;

}
