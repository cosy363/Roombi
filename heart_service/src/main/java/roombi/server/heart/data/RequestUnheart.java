package roombi.server.heart.data;

import lombok.Data;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

@Data
public class RequestUnheart {

    @NotNull(message = "heart id must not be empty.")
    private Long heartId;
}
