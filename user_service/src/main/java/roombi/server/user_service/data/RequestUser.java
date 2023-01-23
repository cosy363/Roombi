package roombi.server.user_service.data;

import lombok.Data;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;


@Data
public class RequestUser {

    @NotNull(message = "ID must not be empty.")
    @Size(min = 2, max = 12, message = "ID must be between 2 and 12 characters.")
    private String userId;

    @NotNull(message = "Password must not be empty.")
    @Size(min = 4, max = 12, message = "Password must be between 2 and 12 characters.")
    private String pwd;
}
