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
  The keys by which a use points at a defined element: its number, its scenario and, as a convenience, its name.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraReferenceV11Mixin  {

  private int fixrId;
  private String fixrName;
  private String fixrScenario;


}