package roombi.server.heart.data;

import lombok.Data;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;


@Data
public class RequestHeart {

    @NotNull(message = "ID must not be empty.")
    @Size(min = 2, max = 12, message = "ID must be between 2 and 12 characters.")
    private String userNumber;

    @NotNull(message = "comb id must not be empty.")
    @Size(min = 4, max = 45, message = "Set combId right")
    private Integer combId;
}
