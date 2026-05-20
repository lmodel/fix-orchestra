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
  This represents the current state of service and session configurations. Changes to configuration can represented with patch operations. See IETF RFC 5261
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Interfaces  {

  private DctermsElementOrRefinementContainer metadata;
  private List<InterfaceType> interface_;


}