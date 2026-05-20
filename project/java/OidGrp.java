package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The identifiers of a message element
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OidGrp  {

  private String abbrName;
  private String scenarioId;
  private String id;
  private String name;
  private String scenario;


}