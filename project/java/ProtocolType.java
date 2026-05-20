package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

@Data
@EqualsAndHashCode(callSuper=false)
public class ProtocolType  {

  private ZonedDateTime activationTime;
  private ZonedDateTime deactivationTime;
  private String layer;
  private URI orchestration;
  private List<String> extraAttributes;
  private InterfaceAnnotation annotation;
  private String name;
  private String version;
  private ZonedDateTime deprecated;
  private String reliability;


}