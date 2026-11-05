package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A field that a message sent by an action sets, or carries over from the message received, by tag number.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraIdentifierV11  {

  private int fixrId;
  private String fixrName;
  private Integer fixrSourceId;


}