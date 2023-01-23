package roombi.server.user_service.data;

import lombok.Data;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

@Data
public class RequestLogin {
    @NotNull(message = "ID cannot be null")
    @Size(min = 2, message = "Please Enter Again")
    private String userId;

    @NotNull(message = "ID cannot be null")
    @Size(min = 4, message = "Password must be longer than 4 characters")
    private String password;
}

