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
  The keys of a defined element, its number, name, short name and scenario.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraIdentityV11Mixin  {

  private int fixrId;
  private String fixrName;
  private String fixrAbbrName;
  private String fixrScenario;


}